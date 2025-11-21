const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from React app in production
if (process.env.NODE_ENV === 'production') {
  app.use(express.static(path.join(__dirname, 'client/build')));
}

// Load flashcard data
const loadFlashcards = () => {
  try {
    const dataPath = path.join(__dirname, 'data', 'flashcards.json');
    const rawData = fs.readFileSync(dataPath, 'utf8');
    return JSON.parse(rawData);
  } catch (error) {
    console.error('Error loading flashcard data:', error);
    return { metadata: {}, flashcards: [] };
  }
};

const flashcardData = loadFlashcards();

// API Routes

// Get all flashcards with optional filtering
app.get('/api/flashcards', (req, res) => {
  const { category, difficulty, search } = req.query;
  let filteredCards = [...flashcardData.flashcards];

  if (category && category !== 'all') {
    filteredCards = filteredCards.filter(card => card.category === category);
  }

  if (difficulty && difficulty !== 'all') {
    filteredCards = filteredCards.filter(card => card.difficulty === difficulty);
  }

  if (search) {
    const searchLower = search.toLowerCase();
    filteredCards = filteredCards.filter(card => 
      card.question.toLowerCase().includes(searchLower) ||
      card.answer.toLowerCase().includes(searchLower) ||
      card.tags.some(tag => tag.toLowerCase().includes(searchLower))
    );
  }

  res.json({
    total: filteredCards.length,
    flashcards: filteredCards
  });
});

// Get metadata
app.get('/api/metadata', (req, res) => {
  res.json(flashcardData.metadata);
});

// Get single flashcard by ID
app.get('/api/flashcards/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const card = flashcardData.flashcards.find(card => card.id === id);
  
  if (card) {
    res.json(card);
  } else {
    res.status(404).json({ error: 'Flashcard not found' });
  }
});

// Get random flashcards
app.get('/api/flashcards/random/:count', (req, res) => {
  const count = parseInt(req.params.count) || 10;
  const shuffled = [...flashcardData.flashcards].sort(() => 0.5 - Math.random());
  res.json(shuffled.slice(0, count));
});

// Get categories
app.get('/api/categories', (req, res) => {
  res.json(flashcardData.metadata.categories || []);
});

// Handle React routing in production
if (process.env.NODE_ENV === 'production') {
  app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
  });
}

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log('Server running on port ' + PORT);
  console.log('Loaded ' + flashcardData.flashcards.length + ' flashcards');
});

module.exports = app;