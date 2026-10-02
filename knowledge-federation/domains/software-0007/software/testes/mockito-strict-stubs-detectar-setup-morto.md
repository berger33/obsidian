---
id: software.testes.tranche10.000374
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: usar STRICT_STUBS para expor stubs desnecessários

## Em uma frase
STRICT_STUBS ajuda a detectar stubs não utilizados e incompatibilidades entre argumentos configurados e invocações reais.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Setup obsoleto pode ocultar mudança no caminho de execução ou deixar fixtures confusas para quem mantém o teste.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Ative strictness no mecanismo de integração escolhido e corrija stubs que não correspondem ao comportamento exercitado.

## Exemplo
O teste configura um método com id A, mas o sistema chama id B; a falha estrita revela a divergência em vez de deixar o setup silencioso.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Strict stubbing pode ter falsos positivos em padrões legítimos de setup compartilhado; não presuma que o modo seja globalmente padrão em toda configuração.

## Como verificar
Introduza um stub não utilizado e um argumento divergente e confirme como o runner sinaliza cada situação na versão adotada.

## Conexões
- [[mockito-matchers-consistencia-em-todos-argumentos]] — Veja também: Mockito: usar matchers em todos os argumentos da chamada.
- [[mockito-lenient-apenas-no-stub-excepcional]] — Veja também: Mockito: limitar lenient a stubs realmente excepcionais.

## Fontes
- [Mockito 5.24.0 — Strictness.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java) — níveis de strictness e benefícios/limitações de STRICT_STUBS; consultado em 2026-10-02.
- [Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java) — integração do Mockito com o ciclo de testes JUnit Jupiter; consultado em 2026-10-02.
