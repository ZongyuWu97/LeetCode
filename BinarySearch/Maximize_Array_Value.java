import java.util.*;

public class Solution {
  public static boolean canAchieveMax(List<Integer> a, int m) {
    int avail = 0;
    for (int el : a) {
        if (el <= m) {
            avail += m - el;
        } else if ((el - avail) <= m) {
            avail -= el - m;
        } else {
            return false;
        }
    }
    return true;
  }


  public static int minimizeMax(List<Integer> a) {
    int i = 0;
    int j = getMax(a);
    int m;
    while (i < j - 1) {
        m = (i + j) / 2;
        if (canAchieveMax(a, m)) {
            j = m;
        } else {
            i = m + 1;
        }
    }
    if (canAchieveMax(a, i)) {
        return i;
    } else {
        return j;
    }
  }

  private static int getMax(List<Integer> a) {
    int res = 0;
    for (int num : a) {
        if (num > res) {
            res = num;
        }
    }
    return res;
  }

    public static void main(String args[]) {
      System.out.println(minimizeMax(new ArrayList<>(Arrays.asList(1, 5, 7, 6))));     //5
      System.out.println(minimizeMax(new ArrayList<>(Arrays.asList(5, 15, 19))));     //15
    }
}