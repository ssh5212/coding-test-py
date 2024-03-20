import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int m;
	static int[][] arr;
	static boolean[][] v;
	
	static class Point {
		int x;
		int y;
		int level;
		
		public Point(int x, int y, int level) {
			this.x = x;
			this.y = y;
			this.level = level;
		}
	}
	
	public static void bfs() {
		Queue<Point> q = new LinkedList<>();
		
		q.add(new Point(0, 0, 1));
		v[0][0] = true;
		
		while(!q.isEmpty()) {
			Point p = q.poll();
			
			if (p.x == n - 1 && p.y == m - 1) {
				System.out.println(p.level);
			}
			
			for (int d = 0; d < 4; d++) {
				int nx = dx[d] + p.x;
				int ny = dy[d] + p.y;
				
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (arr[nx][ny] == 0) continue;
				if (v[nx][ny] == true) continue;
				
				q.add(new Point(nx, ny, p.level + 1));
				v[nx][ny] = true;
				
			}
			
		}
	}
	
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		arr = new int[n][m];
		v = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());		
			String[] s = st.nextToken().split("");
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(s[j]);
			}
		}
		
		bfs();
	}

}