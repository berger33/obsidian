---
id: software.testes.tranche11.000476
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: declarar argumentos de keyword como interface de teste

## Em uma frase
User keywords podem receber argumentos nomeados ou posicionais e podem expor valores de retorno a outras keywords.

## Por que importa
Robot Framework interpreta arquivos de teste por seções e executa keywords de bibliotecas ou recursos; a legibilidade da suíte depende de escopo de variáveis, setup e teardown bem delimitados. Keyword com muitos parâmetros posicionais é fácil de chamar em ordem errada, produzindo cenário que parece válido mas configura outro dado.

## Como funciona
Modele cada caso pelo comportamento observável, mantenha preparações e limpeza no nível apropriado, use tags e templates para organização explícita e prefira keywords de domínio em vez de fluxo condicional espalhado. Use nomes explícitos em parâmetros importantes e converta valores na fronteira da keyword, mantendo defaults visíveis.

## Exemplo
Uma keyword “Criar Pedido” recebe customer_id=... e currency=... e devolve order_id usado em uma assertion subsequente.

## Limites e trade-offs
Keywords e bibliotecas externas têm ciclo de vida e estado próprios; um teardown não desfaz efeitos fora do ambiente de teste. O formato de dados não torna automaticamente um teste independente ou determinístico. A conversão de tipos e sintaxe dependem da keyword/library; não presuma coerção segura para conteúdo arbitrário.

## Como verificar
Inverta dois argumentos propositalmente e confirme que a assinatura ou assertion detecta erro com mensagem compreensível.

## Conexões
- [[robot-resource-vs-library-import]] — Veja também: Robot Framework: distinguir resource file de test library.
- [[robot-ignore-error-nao-esconder-falha]] — Veja também: Robot Framework: limitar Run Keyword And Ignore Error a erro esperado.

## Fontes
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
