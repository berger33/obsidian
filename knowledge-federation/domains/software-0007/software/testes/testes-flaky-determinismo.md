---
id: software.testes.flaky-tests.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://ar5iv.labs.arxiv.org/html/2212.00908", "https://abseil.io/resources/swe-book/html/ch23.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Flaky test, Teste flaky, Teste não determinístico]
lote: software-testes-2000-0001
---

# Testes flaky e determinismo

## Em uma frase
Um teste flaky produz resultados inconsistentes sem uma mudança correspondente no código ou nas condições que deveria estar testando.

## Por que importa
Falhas intermitentes consomem tempo de investigação e podem diminuir a confiança da equipe nos resultados do CI. Se desenvolvedores passam a ignorar falhas ou a repetir testes até obter verde, um defeito real pode ficar oculto junto com o ruído. Reexecuções ajudam a detectar inconsistência, mas não explicam nem corrigem sua causa.

## Como funciona
Um teste pode variar por dependência externa instável, dados compartilhados entre casos, ordem de execução, concorrência, temporização ou ambiente. A revisão multivocal define testes flaky como testes de resultado não determinístico e organiza a literatura por causas, detecção, impacto e respostas; entre as causas discutidas estão dependência da ordem, estado compartilhado e concorrência. O capítulo de CI em Software Engineering at Google descreve como a instabilidade prejudica o feedback e como reexecuções podem ser usadas como sinal adicional, sem substituir o diagnóstico. É útil registrar tentativas e taxas de falha, preservar logs e separar uma falha determinística de um resultado intermitente antes de decidir como o teste afeta o gate.

## Exemplo
Um teste passa quando executado sozinho, mas falha quando roda em paralelo porque dois casos escrevem no mesmo arquivo temporário. Aumentar um `sleep` pode mascarar o problema sem garantir correção. Isolar o diretório de cada teste, controlar o relógio ou esperar por uma condição observável pode atacar a causa, dependendo do diagnóstico.

## Limites e trade-offs
Nem toda falha rara é defeito do teste: sistemas concorrentes podem revelar condições reais da aplicação, e um teste end-to-end pode expor instabilidade de dependência. Repetição automática não deve descartar a falha original; decisões de retry, quarentena e bloqueio devem conservar telemetria e prazo de correção. Reduzir variância sem reduzir a cobertura do risco requer entender a finalidade do teste.

## Como verificar
Execute o teste repetidamente e em ordem aleatória ou paralela, guardando código, ambiente, seed, logs e resultados de cada tentativa. Compare execução isolada com a suíte completa; examine rede, relógio, estado global, concorrência e setup/teardown. Se houver retry, conte e reporte a falha inicial em vez de transformar qualquer sucesso posterior em aprovação silenciosa.

## Conexões
- [[testes-hermeticos-dependencias]] — reduzir dependências ambientais ajuda na reprodutibilidade.
- [[fixtures-pytest-ciclo-vida-escopos]] — setup e escopo de fixtures podem compartilhar estado entre casos.
- [[mutation-testing-eficacia-testes]] — uma suíte estável também precisa demonstrar que detecta comportamentos errados.

## Fontes
- [Rasheed et al. — Test Flakiness’ Causes, Detection, Impact and Responses: A Multivocal Review](https://ar5iv.labs.arxiv.org/html/2212.00908) — define flakiness como resultado não determinístico e sintetiza causas, detecção, impacto e respostas; acesso em 2026-10-01.
- [Software Engineering at Google — CI Challenges e Hermetic Testing](https://abseil.io/resources/swe-book/html/ch23.html) — descreve flakiness, impacto na confiança, repetição de testes e a contribuição da hermeticidade; acesso em 2026-10-01.
