---
id: software.testes.tranche16.001055
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://hurl.dev/docs/hurl-file.html", "https://github.com/Orange-OpenSource/hurl"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: reconhecer o escopo da verificação de contrato

## Em uma frase
Os arquivos verificam forma e valores das respostas que o serviço realmente devolve, sem validar a especificação nem substituir testes de comportamento.

## Por que importa
Usar arquivos de requisição como única verificação deixa regras de negócio complexas sem cobertura e transfere ao contrato responsabilidade que ele não tem.

## Como funciona
Cubra com arquivos os pontos de integração e os contratos acordados, e mantenha testes de comportamento para regras internas e efeitos colaterais.

## Exemplo
Verificar que um pedido retorna o estado esperado não confirma cálculo de preço, arredondamento nem política de desconto aplicada internamente.

## Limites e trade-offs
Arquivos atualizados junto do código podem mascarar mudança incompatível, porque a expectativa passa a descrever o comportamento novo em vez do acordado.

## Como verificar
Compare a expectativa do arquivo com a especificação acordada e trate alterações de contrato como decisão revisada, não como ajuste automático de teste.

## Conexões
- [[hurl-ci-integration]] — Veja também: Hurl: usar o resultado como verificação de esteira.

## Fontes
- [Hurl — File format](https://hurl.dev/docs/hurl-file.html) — estrutura de entradas, resposta esperada, opções e escopo de sessão; consultado em 2026-10-03.
- [Hurl — repositório oficial](https://github.com/Orange-OpenSource/hurl) — visão geral do projeto, exemplos e documentação complementar; consultado em 2026-10-03.
