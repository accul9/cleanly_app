import React, { useState } from "react";
import "./Login.css";

function Login() {
  const [loginId, setLoginId] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("ログインID:", loginId, "パスワード:", password);
    // ログイン処理をここに実装
  };

  return (
    <div>
      <h1>ログイン</h1>
      <form onSubmit={handleLogin}>
        <div>
          <label htmlFor="loginId">ログインID（メールアドレス）:</label>
          <input
            type="email"
            id="loginId"
            value={loginId}
            onChange={(e) => setLoginId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">パスワード:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">ログイン</button>
      </form>
      <p>
        新規ユーザの方は <a href="/signup">こちら</a> から登録してください。
      </p>
    </div>
  );
}

export default Login;
