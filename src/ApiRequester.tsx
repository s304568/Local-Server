import axios from "axios";
import { useState } from "react";

function ApiRequester() {
  const [responseText, setResponseText] = useState("");

  const handleClick = async () => {
    setResponseText("");
    try {
      const response = await axios.get("http://127.0.0.1:5000/animals");
      setResponseText(JSON.stringify(response.data));
    } catch (error) {
      if (axios.isAxiosError(error)) {
        setResponseText(error.message);
      } else {
        setResponseText(String(error));
      }
    }
  };

  return (
    <>
      <div className="Form-Box">
        <form>
          <label>
            <input type="text" />
          </label>
        </form>
        <button type="button" onClick={handleClick}>
          Send Request
        </button>
        {responseText && <p>Response: {responseText}</p>}
      </div>
    </>
  );
}

export default ApiRequester;
