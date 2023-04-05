import React from "react";

function LoginBox() {
    return
    (
      <div>
        <p>Username:</p>
        <input type="text" value={value} onChange={handleChange} />
        <p>You typed: {value}</p>
    
        <p>Password:</p>
        <input type="text" value={value} onChange={handleChange} />
        <p>You typed: {value}</p>
      </div>
    );
  }

  export default LoginBox;