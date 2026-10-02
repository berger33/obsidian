---
id: software.testes.tranche15.000872
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

# Supertest: enviar corpo JSON com send

## Em uma frase
Chamar `.send()` com um objeto faz o Superagent serializar o conteúdo como JSON e definir o cabeçalho de tipo de conteúdo correspondente.

## Por que importa
Montar o corpo manualmente e esquecer o cabeçalho cria requisições que o servidor interpreta como formulário, gerando erro de validação que não corresponde ao cenário testado.

## Como funciona
Passe o objeto diretamente para `.send()` quando o contrato for JSON e use `set` apenas para cabeçalhos adicionais que fazem parte do caso.

## Exemplo
`await request(app).post('/pedidos').send({ item: 'livro', quantidade: 2 }).expect(201);` envia JSON com tipo correto sem configuração extra.

## Limites e trade-offs
O envio automático não valida o corpo contra o schema do servidor nem substitui a asserção sobre a resposta; tipos aninhados e campos opcionais continuam merecendo casos próprios.

## Como verificar
Inspecione o cabeçalho recebido no servidor de teste e confirme que um corpo inválido produz o erro de validação esperado, e não erro de formato.

## Conexões
- [[supertest-chained-expectations]] — Veja também: Supertest: encadear expectativas de resposta.
- [[supertest-end-callback-error-handling]] — Veja também: Supertest: decidir entre callback e promessa.

## Fontes
- [Supertest — pacote npm](https://www.npmjs.com/package/supertest) — exemplos de request, expect, agent e asserções de resposta; consultado em 2026-10-02.
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
