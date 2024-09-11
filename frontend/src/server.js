import axios from 'axios'
const url = "http://127.0.0.1:8000"

export async function getHabitants() {
   return (await axios.get(url+ "/proprietes/habitants"))
}