---
id: software.testes.tranche10.000375
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
fontes: ["https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mockito: limitar lenient a stubs realmente excepcionais

## Em uma frase
Lenient permite que um stub escape de verificações estritas como unused stubbing ou argumento potencialmente incorreto.

## Por que importa
Mocks tornam dependências controláveis em testes unitários, mas stubs e verificações excessivos podem acoplar a suíte a detalhes internos. Aplicar leniency ao teste inteiro pode silenciar problemas em stubs que deveriam falhar cedo.

## Como funciona
Configure somente comportamentos necessários, verifique interações relevantes para o contrato e mantenha o lifecycle e a strictness explícitos. Mantenha strictness como padrão e marque como lenient somente a configuração compartilhada cujo uso opcional seja legítimo.

## Exemplo
Um stub comum de autenticação é lenient em um cenário que nem sempre o usa; o stub específico da regra permanece estrito.

## Limites e trade-offs
Um mock descreve apenas o comportamento programado para o teste; não demonstra compatibilidade, persistência ou semântica da dependência real. Lenient reduz diagnósticos e não corrige o motivo de uma dependência estar sendo configurada sem necessidade.

## Como verificar
Remova a exceção e observe se a mensagem estrita identifica um setup realmente opcional ou um defeito de cenário.

## Conexões
- [[mockito-strict-stubs-detectar-setup-morto]] — Veja também: Mockito: usar STRICT_STUBS para expor stubs desnecessários.
- [[mockito-spy-metodo-real-e-efeitos-colaterais]] — Veja também: Mockito: considerar execução real ao configurar um spy.

## Fontes
- [Mockito 5.24.0 — Strictness.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java) — níveis de strictness e benefícios/limitações de STRICT_STUBS; consultado em 2026-10-02.
- [Mockito 5.24.0 — Mockito.java (repositório oficial)](https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java) — stubbing, verificação, matchers, spies e APIs de Mockito; consultado em 2026-10-02.
