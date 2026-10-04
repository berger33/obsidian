---
id: software.testes.tranche12.000603
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://docs.phpunit.de/en/12.5/attributes.html", "https://docs.phpunit.de/en/12.5/textui.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: usar `Depends` para transferir resultado

## Em uma frase
`#[Depends]` declara que um teste consome o valor retornado por outro teste, mas não define sozinho a ordem de execução dos métodos.

## Por que importa
Esse mecanismo pode expressar uma relação entre producer e consumer, porém transforma um caso em pré-condição do outro e amplia o impacto de qualquer falha no primeiro.

## Como funciona
Reserve dependências para resultados que fazem parte do fluxo de teste, valide o dado recebido no consumidor e use `--order-by depends` quando a ordem do runner precisar satisfazer essas relações.

## Exemplo
Um teste cria um objeto imutável e o retorna; o teste dependente recebe esse objeto para verificar uma transformação posterior.

## Limites e trade-offs
Quando o teste fornecedor falha, o dependente é pulado; sem ordenação de dependências, o consumidor ainda pode ser descoberto antes da origem.

## Como verificar
Force falha na origem e compare a execução padrão com `--order-by depends`; confirme se ambos os casos poderiam criar seus próprios dados sem passar resultado entre métodos.

## Conexões
- [[phpunit-testwith-inline-cases]] — Veja também: PHPUnit 12.5: escolher entre `TestWith` e Data Provider.
- [[phpunit-fixtures-per-test]] — Veja também: PHPUnit 12.5: dimensionar fixtures por teste.

## Fontes
- [PHPUnit 12.5 — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos #[Test], #[DataProvider], #[TestWith], #[Depends] e configurações; consultado em 2026-10-02.
- [PHPUnit 12.5 — Text UI](https://docs.phpunit.de/en/12.5/textui.html) — ordenação, seleção, sementes aleatórias e saída do test runner; consultado em 2026-10-02.
