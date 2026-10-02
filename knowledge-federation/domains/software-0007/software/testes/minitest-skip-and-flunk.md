---
id: software.testes.tranche15.000888
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
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Test.html", "https://docs.seattlerb.org/minitest/Minitest/Assertions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: usar skip e flunk com intenção

## Em uma frase
`skip` interrompe o caso com motivo e o registra como pulado, enquanto `flunk` falha de propósito para marcar um caminho que nunca deveria ser alcançado.

## Por que importa
Marcar indisponibilidade como falha ou esconder teste quebrado com skip indefinido distorce o sinal da suíte e atrasa a correção.

## Como funciona
Use skip com motivo e prazo para dependência externa temporária e reserve flunk para ramos de guarda cuja execução indica erro de construção do teste.

## Exemplo
`skip 'depende de serviço externo' unless ENV['CI_EXTRA']` documenta a condição, e `flunk 'ramo impossível alcançado'` protege uma decisão de controle.

## Limites e trade-offs
Pulados não contam como cobertura e podem se acumular silenciosamente; um flunk mal colocado vira falha artificial quando o comportamento passa a ser válido.

## Como verificar
Rode a suíte e confira a contagem de pulados; reduza a condição do skip e verifique se o caso executa quando a dependência está disponível.

## Conexões
- [[minitest-random-order-and-seed]] — Veja também: Minitest: reproduzir a ordem aleatória.
- [[minitest-reporters-and-run]] — Veja também: Minitest: escolher a forma de execução.

## Fontes
- [Minitest — Test](https://docs.seattlerb.org/minitest/Minitest/Test.html) — classes de teste, ciclos de vida, ordem aleatória e paralelização; consultado em 2026-10-02.
- [Minitest — Assertions](https://docs.seattlerb.org/minitest/Minitest/Assertions.html) — asserções de igualdade, exceções, saída, predicados e tipos; consultado em 2026-10-02.
