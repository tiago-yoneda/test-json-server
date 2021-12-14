const app = require('./src/app');

const PORT = process.env.PORT || 3001;
app.server.listen(PORT, () => {
  console.log('🚀🚀🚀JSON Server is running🚀🚀🚀');
})
