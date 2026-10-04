---
id: software.testes.tranche12.000604
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
fontes: ["https://docs.phpunit.de/en/12.5/fixtures.html", "https://docs.phpunit.de/en/12.5/xml-configuration-file.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: dimensionar fixtures por teste

## Em uma frase
O PHPUnit cria uma instância da classe de teste por método; `setUp()` e `tearDown()` rodam em cada caso, enquanto `setUpBeforeClass()` e `tearDownAfterClass()` cobrem o ciclo da classe.

## Por que importa
Fixtures pequenas tornam o estado inicial visível e reduzem a chance de um teste passar apenas porque outro deixou dados compartilhados.

## Como funciona
Crie no setup somente objetos necessários ao caso; implemente teardown quando houver arquivos, sockets, variáveis de ambiente ou estado externo que exija reversão explícita.

## Exemplo
Uma fixture cria um cliente com stub por método e remove um arquivo temporário em `tearDown`, mantendo o estado de cada caso isolado.

## Limites e trade-offs
Resetar campos de objeto já destruído não acelera coleta de lixo; limpeza excessiva pode ocultar quem é dono do recurso externo.

## Como verificar
Execute o caso sozinho e no conjunto, injete falha antes do fim e confirme que recursos externos são liberados sem alterar o próximo método.

## Conexões
- [[phpunit-depends-retorno]] — Veja também: PHPUnit 12.5: usar `Depends` para transferir resultado.
- [[phpunit-config-precedencia]] — Veja também: PHPUnit 12.5: resolver configuração efetiva.

## Fontes
- [PHPUnit 12.5 — Fixtures](https://docs.phpunit.de/en/12.5/fixtures.html) — setup/teardown, ciclo de vida, estado externo e fixtures compartilhadas; consultado em 2026-10-02.
- [PHPUnit 12.5 — XML Configuration](https://docs.phpunit.de/en/12.5/xml-configuration-file.html) — configuração de grupos, isolamento, execução e resultado; consultado em 2026-10-02.
