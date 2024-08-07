import {
	TextInput,
	PasswordInput,
	Checkbox,
	Anchor,
	Paper,
	Title,
	Text,
	Container,
	Group,
	Button,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { DashBaseProps } from 'props/dash';
import React, { FC } from 'react';
interface Props extends DashBaseProps {

	/**
	 * 登录链接
	 */
	loginUrl: string;
	/**
	 * 在表单上方显示的消息
	 */
	welcomeMessage?: string;

	/**
	 * 是否允许用户注册
	 */
	allowsSignup?: boolean;

	/**
	 * 用户名类型
	 */

	usernameType?: UsernameType;

	/**
	 * 允许找回密码
	 */
	allowsForgotPassword?: boolean;



}

class LoginResponse {

	/** 是否登录成功 */
	success: boolean;

	/** 登录失败时的错误消息 */
	message?: string;

	/** 登录成功后的重定向地址 */
	redirectUrl?: string;
}


enum UsernameType {
	Email = 'email',
	Username = 'username'
}

const UsernameTypes = {
	[UsernameType.Email]: {
		label: '邮箱',
		placeholder: 'you@mantine.dev'
	},

	[UsernameType.Username]: {
		label: '用户名',
		placeholder: '请输入用户名'
	}

}

const UsernamePasswordLogin: FC<Props> = ({
	loginUrl,
	welcomeMessage = '欢迎回来!',
	allowsSignup = false,
	usernameType = UsernameType.Username,
	allowsForgotPassword = false
}) => {

	const getUsernameValidation = () => {
		if (usernameType === UsernameType.Email) {
			return (value: string) => (/^\S+@\S+$/.test(value) ? null : '请输入有效的邮箱地址')
		}
		else if (usernameType === UsernameType.Username) {
			return (value: string) => (value.length > 0 ? null : '请输入用户名')
		}
		throw new Error('无效的用户名类型')
	}


	const form = useForm({
		mode: 'uncontrolled',
		initialValues: {
			[usernameType]: '',
			password: '',
		},

		validate: {
			[usernameType]: getUsernameValidation(),
			password: (value) => (value.length > 0 ? null : '请输入密码'),
		},
	});

	const login = async (values: Record<string, string>) => {
		const response = await fetch(loginUrl, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(values)
		});

		const data = await response.json() as LoginResponse;

		if (data.success) {
			window.location.href = data.redirectUrl;
		}
		else {
			alert(data.message);
		}

	}

	return (
		<form onSubmit={form.onSubmit((values) => login(values))}>
			<Container size={420} my={40}>
				<Title ta="center" >
					{welcomeMessage}
				</Title>
				{
					allowsSignup && (
						<Text c="dimmed" size="sm" ta="center" mt={5}>
							还没有账号?{' '}
							<Anchor size="sm" component="button">
								立即创建
							</Anchor>
						</Text>
					)
				}
				<Paper withBorder shadow="md" p={30} mt={30} radius="md">
					<TextInput withAsterisk label={UsernameTypes[usernameType].label} placeholder={UsernameTypes[usernameType].placeholder}
						key={form.key(usernameType)}
						{...form.getInputProps(usernameType)}
					/>
					<PasswordInput withAsterisk label="密码" placeholder="请输入密码" mt="md"
						key={form.key('password')}
						{...form.getInputProps('password')}
					/>
					<Group justify="space-between" mt="lg">
						<Checkbox label="记住我" />

						{
							allowsForgotPassword && (
								<Anchor component="button" size="sm">
									忘记密码?
								</Anchor>
							)
						}
					</Group>
					<Button type='submit' fullWidth mt="xl">
						登录
					</Button>
				</Paper>
			</Container>
		</form>
	);
}

export default UsernamePasswordLogin;