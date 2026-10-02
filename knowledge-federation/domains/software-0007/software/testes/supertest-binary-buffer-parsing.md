---
id: software.testes.tranche15.000877
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

# Supertest: verificar respostas binárias

## Em uma frase
Respostas que não são JSON chegam ao teste como fluxo ou buffer, e a verificação precisa olhar bytes e cabeçalhos em vez de assumir corpo estruturado.

## Por que importa
Tratar download de arquivo como se fosse JSON produz corpo vazio e induz a concluir que o endpoint falhou, quando o formato é apenas diferente do esperado.

## Como funciona
Confirme o tipo de conteúdo, force o armazenamento em buffer quando necessário e compare tamanho ou assinatura do arquivo em vez do corpo interpretado.

## Exemplo
`const resposta = await request(app).get('/relatorio.pdf').buffer(true); expect(resposta.headers['content-type']).toContain('pdf'); expect(resposta.body.length).toBeGreaterThan(0);` valida o artefato.

## Limites e trade-offs
Comparar o conteúdo binário inteiro é frágil porque geradores podem incorporar data ou metadados; a asserção deve focar no contrato estável do formato.

## Como verificar
Baixe o mesmo artefato duas vezes e verifique cabeçalhos e integridade; para formatos conhecidos, valide a assinatura inicial dos bytes.

## Conexões
- [[supertest-timeouts]] — Veja também: Supertest: limitar tempo de resposta em teste.
- [[supertest-server-lifecycle]] — Veja também: Supertest: entender o ciclo do servidor efêmero.

## Fontes
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
- [Supertest — repositório oficial](https://github.com/ladjs/supertest) — README, opções de uso e integração com servidores e agentes; consultado em 2026-10-02.
