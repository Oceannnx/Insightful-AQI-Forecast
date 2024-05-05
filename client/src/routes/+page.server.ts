// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const load = ({ cookies }: { cookies: any }) => {
	const visited = cookies.get('visited');

	cookies.set('visited', 'true', { path: '/' });

	return {
		visited
	};
};
