import React, { useState } from "react";
import "./Login.css";
import axios from "axios";

function Login() {
  const [loginId, setLoginId] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/login/",
        {
          email: loginId,
          password: password,
        },
        {
          withCredentials: true, // セッションCookieを利用
        }
      );
      console.log("ログイン成功:", response.data);
      setErrorMessage("");
      // 必要に応じてリダイレクト処理や状態管理を追加
    } catch (error) {
      console.error("ログイン失敗:", error.response?.data || error.message);
      setErrorMessage("ログインに失敗しました。正しい情報を入力してください。");
    }
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
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        <button type="submit">ログイン</button>
      </form>
      <p>
        新規ユーザの方は <a href="/signup">こちら</a> から登録してください。
      </p>
    </div>
  );
}

export default Login;