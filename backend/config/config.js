module.exports = {
  development: {
    database: {
      url: process.env.DATABASE_URL || 'sqlite:///markai_dev.db'
    },
    jwt: {
      secret: process.env.JWT_SECRET || 'dev_secret',
      expiresIn: '1h'
    }
  },
  production: {
    database: {
      url: process.env.DATABASE_URL
    },
    jwt: {
      secret: process.env.JWT_SECRET,
      expiresIn: '1h'
    }
  }
};