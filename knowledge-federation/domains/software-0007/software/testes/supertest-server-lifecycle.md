---
id: software.testes.tranche15.000878
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
fontes: ["https://github.com/ladjs/supertest", "https://expressjs.com/en/guide/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: entender o ciclo do servidor efêmero

## Em uma frase
Ao receber a aplicação, o Supertest inicia um servidor em porta efêmera para a requisição e o encerra ao final, dispensando gerenciamento manual de porta na maioria dos casos.

## Por que importa
Subir um servidor fixo por suíte cria porta compartilhada e encerramento frágil, enquanto deixar conexões abertas impede o processo de teste de terminar.

## Como funciona
Passe a aplicação diretamente ao Supertest, evite escutar porta fixa para testes comuns e, quando precisar de servidor persistente, garanta o encerramento no hook final.

## Exemplo
`request(app)` é suficiente para disparar a chamada; já `request(servidor)` exige que alguém tenha chamado `listen` e que o fechamento ocorra depois dos testes.

## Limites e trade-offs
Servidores persistentes são necessários para clientes externos, WebSocket ou múltiplas origens, mas trazem custo de porta, limpeza e isolamento que a porta efêmera não tem.

## Como verificar
Rode a suíte e confirme que o processo encerra sozinho; depois use um servidor persistente de propósito e verifique que ele é fechado ao final.

## Conexões
- [[supertest-binary-buffer-parsing]] — Veja também: Supertest: verificar respostas binárias.
- [[supertest-against-express-router]] — Veja também: Supertest: testar a aplicação no limite certo.

## Fontes
- [Supertest — repositório oficial](https://github.com/ladjs/supertest) — README, opções de uso e integração com servidores e agentes; consultado em 2026-10-02.
- [Express — Testing](https://expressjs.com/en/guide/testing.html) — orientações e exemplos de teste de aplicações Express; consultado em 2026-10-02.
