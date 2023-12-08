import axios from "axios";
import { useState } from "react";

function ApiRequester() {
  const [responseText, setResponseText] = useState("");

  const handleClick = async () => {
    setResponseText("");
    try {
      const response = await axios.get("URL");
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
      <button type="button" onClick={handleClick}>
        Send Request
      </button>
      {responseText && <p>Response: {responseText}</p>}
    </>
  );
}

export default ApiRequester;
