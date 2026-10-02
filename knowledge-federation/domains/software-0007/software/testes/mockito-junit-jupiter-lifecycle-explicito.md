---
id: software.testes.tranche10.000379
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: registrar a extensão JUnit Jupiter para inicializar mocks

## Em uma frase
MockitoExtension integra criação de mocks anotados e sessão Mockito ao lifecycle de testes Jupiter.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Misturar inicialização manual e extensão pode duplicar configuração e tornar difícil saber quando o estado é limpo.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Registre MockitoExtension com @ExtendWith e deixe a criação do SUT explícita quando isso melhora a leitura das dependências.

## Exemplo
A classe registra a extensão, recebe @Mock no colaborador e constrói o serviço no setup a partir desse mock.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. A anotação @InjectMocks não substitui um teste de composição real nem garante que a construção da aplicação esteja correta.

## Como verificar
Remova o registro da extensão para confirmar que o setup não depende de inicialização implícita não declarada.

## Conexões
- [[mockito-nao-compartilhar-mock-mutavel-entre-testes]] — Veja também: Mockito: preferir mocks novos a resetar estado compartilhado.

## Fontes
- [Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java) — integração do Mockito com o ciclo de testes JUnit Jupiter; consultado em 2026-10-02.
- [Mockito 5.24.0 — Strictness.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java) — níveis de strictness e benefícios/limitações de STRICT_STUBS; consultado em 2026-10-02.
