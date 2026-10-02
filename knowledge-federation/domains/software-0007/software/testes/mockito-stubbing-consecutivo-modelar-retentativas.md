---
id: software.testes.tranche10.000377
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: usar stubbing consecutivo para sequência legítima

## Em uma frase
Stubbing consecutivo define respostas diferentes para chamadas subsequentes do mesmo método.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Retentativas, paginação ou polling podem exigir uma resposta temporária seguida por uma resposta final em uma única execução.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Configure a sequência somente quando o contrato prevê múltiplas chamadas e verifique o estado final ou a política de retry.

## Exemplo
A primeira leitura do endpoint retorna indisponível e a segunda retorna sucesso, exercitando o limite de tentativas do cliente.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Uma sequência de respostas pode mascarar excesso de chamadas se o teste não afirmar também o número máximo permitido.

## Como verificar
Adicione uma chamada extra e confirme se o comportamento permanece válido ou se o teste detecta retry além do limite.

## Conexões
- [[mockito-spy-metodo-real-e-efeitos-colaterais]] — Veja também: Mockito: considerar execução real ao configurar um spy.
- [[mockito-nao-compartilhar-mock-mutavel-entre-testes]] — Veja também: Mockito: preferir mocks novos a resetar estado compartilhado.

## Fontes
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
- [Mockito 5.24.0 — Strictness.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java) — níveis de strictness e benefícios/limitações de STRICT_STUBS; consultado em 2026-10-02.
