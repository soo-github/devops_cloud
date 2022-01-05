import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '2022년에는 운동하기', color: 'blue' },
  { content: '파이썬 익히기', color: 'red' },
  { content: '리액트 익히기', color: 'red' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'red',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const appendTodo = () => {
    console.log('새로운 todo를 추가하겠습니다.');
    const todo = { ...fieldValues };

    setTodoList((prevTodoList) => [...prevTodoList, todo]);

    clearFieldValues();
  };

  // const changeInputText = (e) => {
  //   setInputText(e.target.value);
  // };

  // const appendInputText = (e) => {
  //   console.log('e.key: ', e.key);
  //   if (e.key === 'Enter') {
  // todoList 배열 끝에 inputText를 추가합니다.
  // inputText를 다시 비웁니다.
  // console.log('inputText: ', inputText);

  // setTodoList에 함수를 넘기는 것.
  // todoList 상탯값을 변경하는 것은 아닙니다.(배열의 push를 사용 X)

  // setTodoList((prevTodoList) => {
  //   return [...prevTodoList, { content: inputText }];
  // });
  // setInputText('');
  //   }
  // };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendTodo}
      />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        className="bg-red-500 text-gray-100 cursur-pointer"
        onClick={() => clearFieldValues()}
      >
        clear
      </button>

      {/* <input
        type="text"
        valu={inputText}
        onChange={changeInputText}
        onKeyPress={appendInputText}
      /> */}

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
        // <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TodoList;
