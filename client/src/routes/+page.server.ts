// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const load = ({ cookies }: { cookies: any }) => {
	const visited = cookies.get('visited');
	const maxAge = 60 * 60 * 24 * 365 * 10;

	cookies.set('visited', 'true', 
	{	path: '/',
		httpOnly: true, 
    	secure: true,   
        maxAge: maxAge
	})  
	return {
		visited
	};
};
