const express = require("express");
const app = express();

app.set("views", "./");
app.set("view engine", "pug");
app.use(express.static(`${__dirname}/public`));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index");
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server is opened at ${PORT}`));
