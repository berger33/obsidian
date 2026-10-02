---
id: software.testes.tranche15.000876
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
fontes: ["https://visionmedia.github.io/superagent/", "https://github.com/ladjs/supertest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: limitar tempo de resposta em teste

## Em uma frase
O cliente herdado do Superagent permite configurar tempo limite por resposta ou por prazo total, evitando que uma suíte fique pendurada indefinidamente.

## Por que importa
Servidores de teste que aceitam conexão, mas nunca respondem, travam o pipeline até o limite global do executor e escondem a rota problemática.

## Como funciona
Defina um tempo limite explícito e curto para testes de contrato e trate a falha como comportamento observável do caso que exercita indisponibilidade.

## Exemplo
`request(app).get('/lento').timeout({ response: 500, deadline: 2000 })` transforma uma espera longa em erro identificável no ponto do consumo.

## Limites e trade-offs
Tempo limite é política de teste e não substitui o timeout do serviço real; valores curtos demais criam falhas intermitentes em máquinas carregadas e exigem margem calibrada.

## Como verificar
Aponte o teste para uma rota que atrasa a resposta além do limite e confirme que o erro citado é de tempo, não de asserção de status.

## Conexões
- [[supertest-auth-headers-set]] — Veja também: Supertest: definir autenticação por cabeçalho.
- [[supertest-binary-buffer-parsing]] — Veja também: Supertest: verificar respostas binárias.

## Fontes
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
- [Supertest — repositório oficial](https://github.com/ladjs/supertest) — README, opções de uso e integração com servidores e agentes; consultado em 2026-10-02.
