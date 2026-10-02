---
id: software.testes.tranche10.000371
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: não verificar automaticamente uma chamada já stubada

## Em uma frase
Stubbing define a resposta de um mock; verificar uma invocação stubada costuma ser redundante quando a saída do sistema já comprova seu uso.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Duplicar setup e verify aumenta o acoplamento sem necessariamente acrescentar evidência de comportamento.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Use when/thenReturn para configurar o cenário e verifique uma interação separada somente se ela própria for requisito.

## Exemplo
O serviço transforma o resultado stubado do repositório e o teste afirma o DTO produzido sem exigir uma verificação redundante do getter.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Alguns efeitos, como envio de mensagem ou comando externo, continuam exigindo verificação porque não aparecem no retorno.

## Como verificar
Remova uma verificação e confirme se alguma propriedade relevante deixa de ser observada no teste.

## Conexões
- [[mockito-verificar-contrato-nao-roteiro-interno]] — Veja também: Mockito: verificar contrato observável do colaborador.
- [[mockito-argumentcaptor-apos-verificacao]] — Veja também: Mockito: capturar argumento durante a verificação.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java) — integração do Mockito com o ciclo de testes JUnit Jupiter; consultado em 2026-10-02.
