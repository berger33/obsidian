---
id: software.testes.tranche15.000870
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.npmjs.com/package/supertest", "https://github.com/ladjs/supertest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: manter sessão com request.agent

## Em uma frase
`request.agent(app)` mantém os cookies recebidos entre chamadas, reproduzindo o comportamento de um cliente que preserva sessão entre requisições.

## Por que importa
Fluxos autenticados dependem de estado que uma requisição isolada não carrega, e recriar cabeçalhos manualmente em cada passo torna o teste sensível a detalhes do mecanismo de sessão.

## Como funciona
Crie um agente por cenário, faça o login uma vez por ele e reutilize o mesmo objeto nas chamadas seguintes para que os cookies sejam reenviados automaticamente.

## Exemplo
`const agente = request.agent(app); await agente.post('/login').send({ usuario: 'ada' }); await agente.get('/perfil').expect(200);` percorre o fluxo autenticado sem copiar cookie algum.

## Limites e trade-offs
O agente compartilha estado entre as chamadas que o utilizam, então dois cenários independentes não devem dividir o mesmo agente; tokens de portador continuam exigindo cabeçalho explícito.

## Como verificar
Faça login, acesse a rota protegida e confirme que uma chamada sem o agente recebe negação, provando que a sessão está no agente e não no servidor global.

## Conexões
- [[supertest-chained-expectations]] — Veja também: Supertest: encadear expectativas de resposta.

## Fontes
- [Supertest — pacote npm](https://www.npmjs.com/package/supertest) — exemplos de request, expect, agent e asserções de resposta; consultado em 2026-10-02.
- [Supertest — repositório oficial](https://github.com/ladjs/supertest) — README, opções de uso e integração com servidores e agentes; consultado em 2026-10-02.
