import React, { useState } from 'react';
import styles from './Login.module.css';
import { useNavigate } from 'react-router-dom';
import { LoginState, UserState } from '../../stores/login-store';
import { useSetRecoilState } from 'recoil';
import axios from '../../utils/axios'; 

export const Login = () => {
  const setIsLoggedIn = useSetRecoilState(LoginState);
  const setUserState = useSetRecoilState(UserState);

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const handleUsernameChange = e => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = e => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/accounts/login/', 
        {
          username: username,
          password: password,
        },
        {
          withCredentials: true,
        }
      );
      // 서버로부터 받은 토큰을 로컬 스토리지에 저장
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);

      console.log('로그인 성공:', response.data);
      navigate('/politics');

      // 로그인 성공 후 처리
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className={styles.container}>
      <img className={styles.image} src="logo.png" alt="로고" />
      <div className={styles.subcontainer}>
        <form className={styles.form}  onSubmit={handleSubmit}>
          <div className={styles.wrapper}>
            <input
              type="username"
              id="username"
              value={username}
              onChange={handleUsernameChange}
              placeholder="아이디"
            />
          </div>
          <div className={styles.wrapper}>
            <input
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              placeholder="비밀번호"
            />
          </div>
          <button
            className={styles.login_button}
            type="submit"
          >
            Login
          </button>
          <div>
            <img src="Line-left.png" /> Or better yet...
            <img src="Line-left.png" />
          </div>
          <button
            className={styles.join_button}
            type="button"
            onClick={() => navigate("/join")}
          >
            Don't you have account? Sign up
          </button>
        </form>
      </div>
    </div>
  );
};