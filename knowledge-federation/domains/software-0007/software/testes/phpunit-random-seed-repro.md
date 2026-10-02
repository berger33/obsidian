---
id: software.testes.tranche12.000607
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
fontes: ["https://docs.phpunit.de/en/12.5/textui.html", "https://docs.phpunit.de/en/12.5/xml-configuration-file.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: reproduzir falhas por ordem aleatória

## Em uma frase
A opção `--order-by random` executa testes em ordem pseudoaleatória e aceita uma seed para repetir a mesma sequência.

## Por que importa
Ordem variável pode expor dependências de estado que permanecem invisíveis quando cada classe parece passar isoladamente.

## Como funciona
Rode periodicamente em modo aleatório, guarde a seed impressa e use-a novamente para investigar antes de alterar fixtures ou ordem manualmente.

## Exemplo
Uma falha que aparece somente após determinado teste pode ser repetida com a seed informada pelo runner e examinada com output de debug.

## Limites e trade-offs
A mesma seed pode não reproduzir todas as fontes de não determinismo, como relógio, concorrência ou dados remotos que mudaram.

## Como verificar
Adicione o comando com a seed ao ticket de falha e confirme se a sequência que a originou é repetida em ambiente equivalente.

## Conexões
- [[phpunit-selection-filter-group]] — Veja também: PHPUnit 12.5: selecionar testes por suite, grupo ou padrão.
- [[phpunit-risky-output-assertions]] — Veja também: PHPUnit 12.5: interpretar testes marcados como risky.

## Fontes
- [PHPUnit 12.5 — Text UI](https://docs.phpunit.de/en/12.5/textui.html) — ordenação, seleção, sementes aleatórias e saída do test runner; consultado em 2026-10-02.
- [PHPUnit 12.5 — XML Configuration](https://docs.phpunit.de/en/12.5/xml-configuration-file.html) — configuração de grupos, isolamento, execução e resultado; consultado em 2026-10-02.
