/* eslint-disable */
import axios from "axios"

const findAnime = async (query) => {
  const path = `http://localhost:5000/search?search=${query}`
  const res = await axios.get(path, {});
  return res.data;
}

export default {
  findAnime
}
