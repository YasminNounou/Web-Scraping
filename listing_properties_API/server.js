const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 5001;

// Load listings from JSON file
const listings = JSON.parse(fs.readFileSync('listings.json'));

// GET /api/listings?priceMin=600&priceMax=1500&location=Cairo
app.get('/api/listings', (req, res) => {
    
  const { priceMin, priceMax, location } = req.query;
  let filtered = listings;
    
  if (priceMin && priceMax) {
    //case of range 
    filtered = filtered.filter(listing => Number(listing.price.replace(/,/g, '')) >= Number(priceMin) && Number(listing.price.replace(/,/g, '')) <= Number(priceMax));
  }
    else if (priceMin) {
    filtered = filtered.filter(listing => Number(listing.price.replace(/,/g, '')) >= Number(priceMin));
  }
  else if (priceMax) {
    filtered = filtered.filter(listing => Number(listing.price.replace(/,/g, '')) <= Number(priceMax));
  }

  if (location) {
    filtered = filtered.filter(listing =>
      listing.location.toLowerCase() === location.toLowerCase()
    );
  }
  res.json(filtered);
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
