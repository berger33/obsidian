---
id: software.seguranca.cookies-sessao.000001
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
aliases: [Cookies de sessão, Secure, HttpOnly, SameSite]
lote: software-seguranca-0003
---

# Cookies seguros para sessões HTTP

## Em uma frase
A segurança de um cookie de sessão depende de proteger o identificador que ele carrega, limitar quando o navegador o envia e controlar o ciclo de vida da sessão no servidor.

## Por que importa
Depois do login, o identificador de sessão normalmente funciona como uma credencial portadora: quem o obtém pode agir como a pessoa autenticada até que a sessão expire ou seja revogada. Flags do cookie reduzem alguns caminhos de exposição, mas não substituem autorização, expiração, rotação ou proteção contra falhas na aplicação.

## Como funciona
`Secure` instrui o navegador a enviar o cookie somente em conexões HTTPS. `HttpOnly` impede que scripts da página leiam o valor por APIs como `document.cookie`, mas não impede que um script malicioso faça requisições autenticadas; portanto, não corrige XSS. `SameSite=Lax` ou `Strict` restringe o envio em certos contextos cross-site e pode reduzir risco de CSRF. Se `SameSite=None` for necessário para um caso cross-site, o cookie também precisa de `Secure`. Para cookies host-only, o prefixo `__Host-` exige `Secure`, `Path=/` e ausência de `Domain`, limitando o compartilhamento com subdomínios. Um exemplo de cabeçalho é `Set-Cookie: __Host-SessionID=...; Secure; HttpOnly; SameSite=Lax; Path=/`.

## Exemplo
Após autenticação, o servidor emite um identificador aleatório e o guarda em um cookie com `Secure`, `HttpOnly`, `SameSite` explícito e escopo restrito. Na autenticação ou elevação de privilégio, a aplicação renova o identificador para evitar preservar um valor escolhido antes da autenticação. No logout, revoga a sessão no servidor e expira o cookie no navegador.

## Limites e trade-offs
`HttpOnly` protege a confidencialidade do cookie contra leitura simples por JavaScript, não contra ações feitas por XSS. `SameSite` é defesa em profundidade, não substituto universal para token anti-CSRF, e pode interferir em fluxos legítimos de entrada ou integração. `Secure` não protege sessões em terminais comprometidos nem valida que a pessoa ainda deve ter acesso. Escolha duração e política de renovação com base no risco e na experiência do produto.

## Como verificar
Inspecione `Set-Cookie` em login, renovação e logout, incluindo atributos, escopo, expiração e rotação do valor. Teste acesso HTTPS, tentativas cross-site relevantes, revogação e expiração. Confirme que autorização é checada no servidor em cada operação sensível.

## Conexões
- [[csrf-token-protecao-web]] — cookies enviados automaticamente pelo navegador influenciam o desenho das defesas anti-CSRF.
- [[cors-origem-nao-autorizacao]] — CORS e SameSite tratam fronteiras diferentes e não são mecanismos de autorização.
- [[oauth-pkce-fluxo-codigo]] — PKCE protege a troca do código; o cookie protege a sessão estabelecida depois.

## Fontes
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — atributos, ciclo de vida e propriedades de identificadores de sessão; acesso em 2026-10-01.
- [MDN — Set-Cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) — sintaxe e comportamento dos atributos de cookie; acesso em 2026-10-01.
