/*
register.html 폼 유효성 검증
jquery validation plug-in 사용
*/
$(function () {
  $("#signup").validate({
    //rules 정하기 - 유효성 검증 규칙 지정
    //폼 요소 이름 사용
    rules: {
      userid: {
        required: true,
        validId: true,
      },
      password: {
        required: true,
        validPwd: true,
      },
      confirm_password: {
        required: true,
        validPwd: true,
        equalTo: "#password", //현재 요소가 어떤 요소랑 값이 같아야 하는가?(아이디 사용)
      },
      gender: {
        required: true,
      },
      email: {
        required: true,
        email: true,
      },
      mobile: {
        required: true,
        validMobile: true,
      },
      hobby: {
        required: true,
      },
    }, //rules 종료

    //규칙이 맞지 않을 경우 보여줄 메세지 작성
    messages: {
      userid: {
        required: "아이디는 필수 입력 요소입니다.",
      },
      password: {
        required: "비밀번호는 필수 입력 요소입니다.",
      },
      confirm_password: {
        required: "비밀번호는 필수 입력 요소입니다.",
        equalTo: "비밀번호를 확인해 주세요",
      },
      gender: {
        required: "성별은 필수 입력 요소입니다.",
      },
      email: {
        required: "이메일은 필수 입력 요소입니다.",
        email: "이메일 형식을 확인해 주세요.",
      },
      mobile: {
        required: "핸드폰 번호는 필수 입력 요소입니다.",
      },
      hobby: {
        required: "취미를 적어도 하나 선택해 주세요.",
      },
    },
  });
});

$.validator.addMethod(
  "validId",
  function (data) {
    const regId = /^(?=.*A-Za-z)(?=.*[0-9])[A-Za-z0-9]{6,12}$/;
    return regId.test(data); //원본데이터인 입력받을 data를 넣어주고 리턴해주기
  },
  "아이디는 영문자,숫자의 조합으로 6~12자리로 만들어야 합니다"
);

$.validator.addMethod(
  "validPwd",
  function (data) {
    const regPwd =
      /^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{8,15}$/;
    return regPwd.test(data); //원본데이터인 입력받을 data를 넣어주고 리턴해주기
  },
  "비밀번호는 영문자,숫자,특수문자의 조합으로 8~15자리로 만들어야 합니다"
);

$.validator.addMethod(
  "validMobile",
  function (data) {
    const regMobile = /^\d{3}\d{4}\d{4}$/;
    return regMobile.test(data); //원본데이터인 입력받을 data를 넣어주고 리턴해주기
  },
  "핸드폰번호를 확인해 주세요(- 제외)"
);
