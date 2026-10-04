---
id: software.testes.tranche15.000874
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
fontes: ["https://www.npmjs.com/package/supertest", "https://visionmedia.github.io/superagent/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: enviar arquivos com attach

## Em uma frase
O método `attach` adiciona uma parte de arquivo a uma requisição multipart, recebendo caminho do documento e campos adicionais do formulário.

## Por que importa
Testar upload apenas com corpo JSON não exercita limites de tamanho, nome de arquivo e campos mistos que o endpoint real precisa tratar.

## Como funciona
Use `attach` para o documento e `field` para os campos de texto, mantendo os arquivos de teste pequenos e versionados junto da suíte.

## Exemplo
`request(app).post('/documentos').field('titulo', 'contrato').attach('arquivo', 'fixtures/contrato.pdf').expect(201);` cobre formulário e arquivo na mesma chamada.

## Limites e trade-offs
Arquivos grandes deixam a suíte lenta e o teste não valida políticas de antivírus ou armazenamento externo, que continuam dependendo do ambiente de integração.

## Como verificar
Envie uma fixture conhecida, confirme o tipo e o tamanho recebidos pelo servidor e teste também a recusa de um arquivo acima do limite.

## Conexões
- [[supertest-end-callback-error-handling]] — Veja também: Supertest: decidir entre callback e promessa.
- [[supertest-auth-headers-set]] — Veja também: Supertest: definir autenticação por cabeçalho.

## Fontes
- [Supertest — pacote npm](https://www.npmjs.com/package/supertest) — exemplos de request, expect, agent e asserções de resposta; consultado em 2026-10-02.
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
