import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      // ユーザー作成のAPI呼び出し
      const response = await axios.post("http://localhost:8000/api/v1/users/", {
        name,
        email,
        password,
      });

      console.log("ユーザー作成成功:", response.data);

      // 自動認証処理（セッションの開始など）
      await axios.post(
        "http://localhost:8000/api/v1/login/",
        {
          username: email, // メールアドレスを認証用に送信
          password,
        },
        {
          withCredentials: true,
          headers: {
            "X-CSRFToken": getCsrfToken(),
          },
        }
      );

      console.log("自動ログイン成功");

      // タスク画面に遷移
      navigate("/task");
    } catch (error) {
      console.error("ユーザー作成または認証に失敗:", error.response?.data || error.message);
      setErrorMessage("ユーザー作成に失敗しました。再度お試しください。");
    }
  };

  return (
    <div>
      <h1>新規ユーザ登録をしてください</h1>
      <form onSubmit={handleSignup}>
        <div>
          <label htmlFor="name">名前:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">メールアドレス:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
        <button type="submit">ユーザ作成</button>
      </form>
      <p>
        登録がお済みの方は <a href="/">こちら</a> からログインしてください。
      </p>
    </div>
  );
}

export default Signup;