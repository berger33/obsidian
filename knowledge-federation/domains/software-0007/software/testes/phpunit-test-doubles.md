---
id: software.testes.tranche18.001201
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://docs.phpunit.de/en/12.5/test-doubles.html", "https://docs.phpunit.de/en/12.5/attributes.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: substituir dependências com dublês

## Em uma frase
O framework cria dublês de tipos, com configuração de retornos, exceções e verificação de chamadas, além de restringir a geração automática de valores.

## Por que importa
Dependências lentas ou externas ficam controladas, e o dublê permite verificar que a colaboração esperada realmente ocorreu.

## Como funciona
Crie o dublê a partir da interface ou classe, configure apenas os métodos usados pelo caso e verifique as expectativas ao final.

## Exemplo
Um repositório pode ser substituído por dublê configurado para devolver a entidade esperada e registrar a chamada de gravação.

## Limites e trade-offs
Dublês de classes concretas acoplam o teste à implementação, e retornos automáticos escondem configurações faltantes.

## Como verificar
Remova a chamada no código de produção e confirme que a verificação de expectativa acusa a ausência da colaboração.

## Conexões
- [[phpunit-fixtures]] — Veja também: PHPUnit: preparar e limpar com métodos de ciclo.
- [[phpunit-coverage]] — Veja também: PHPUnit: medir e interpretar cobertura.

## Fontes
- [PHPUnit — Test doubles](https://docs.phpunit.de/en/12.5/test-doubles.html) — dublês de tipos, configuração de retornos e verificação de chamadas; consultado em 2026-10-03.
- [PHPUnit — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos de teste, provedores, grupos e configuração de dublês; consultado em 2026-10-03.
