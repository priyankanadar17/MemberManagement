export enum MemberType {
    Alumnus = 're',
    Friend_Of_The_Association = 'fr',
    Faculty_Or_Staff = 'fs',
}

export function getAllowedTiers(type?: MemberType): MemberTier[] {
    if (type !== undefined && type !== MemberType.Alumnus) {
        return [MemberTier.Contributor, MemberTier.Parton];
    }

    return [MemberTier.Starter, MemberTier.Contributor, MemberTier.Parton];
}

export const MemberTypeDescriptions: Record<MemberType, string> = {
    re: 'Alumnus',
    fr: 'Friend Of The Association',
    fs: 'Faculty Or Staff',
};

export enum MemberTier {
    Starter = 'st',
    Contributor = 'co',
    Parton = 'pa',
}

export const MemberTierShortTitles: Record<MemberTier, string> = {
    st: 'Starter – Free Membership for 0€ p.a.',
    co: 'Contributor – Standard membership for 39€ p.a.',
    pa: 'Patron – Premium membership for 249€ p.a.',
}
export const MemberTierTitles: Record<MemberTier, string> = {
    st: '<b>Starter</b> - The free membership for those not ready or willing to financially contribute to the Association at this point. ',
    co: '<b>Contributor</b> - Our standard membership for Alumni and associate members who are part of the Jacobs community.',
    pa: '<b>Patron</b> - Our membership for senior alumni and friends who want to give back even more and love to see the Jacobs spirit grow!',
}

export const MemberTierDescriptions: Record<MemberTier, string> = {
    st: `
        We want all Alumni to be able to connect via the Association and won't exclude anyone based on their financial situation or willingness to contribute.
        After the first 2 years (and then once a year after that), we'll check with you if you want to stay in the Starter tier or if you feel comfortable upgrading to one of our paid tiers.
        If you don't, no problem, you can decide to stay in the Starter tier with no disadvantages.
    `,
    co: `
    <ul>
        <li>Your @jacobs-alumni.de email account is hosted on G Suite and comes with access to various apps as well as unlimited Google Drive space. </li>
        <li>Voting rights in the General Assembly of the Jacobs Alumni Association. </li>
        <li>Eligibility as a mentee or mentor for 1 year mentoring program. </li>
        <li>Access to Career Counselling Services. </li>
        <li>Free access to career seminars and workshops (on campus). </li>
        <li>Jacobs Career Fair: Free Silver Package (worth 850€) for own start-ups and spin-off companies.</li>
        <li>Career Services for Alumni Employers: 20% discount on Presentations, Recruiting Events, Workshops, Employer Interviews and Pre-Selection.</li>
        <li>Alumni Newsletter to stay up-to-date on all Alumni and University developments</li>
        <li>More to come!</li>
    </ul>
    `,
    pa: `
        Includes all benefits of the Contributor membership PLUS:
        <ul>
            <li>After three years of patron membership, engraved alumni brick (on the path in front of the IRC)</li>
            <li>Special mention in the Association’s newsletter after joining</li>
            <li>Special mention in yearly newsletter every year of membership</li>
            <li>Enables the Alumni Association to help young and future alumni grow and really make a difference in their lives</li>
        </ul>
    `,
}