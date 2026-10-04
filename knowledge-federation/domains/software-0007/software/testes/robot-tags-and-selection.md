---
id: software.testes.tranche17.001080
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: etiquetar e selecionar testes

## Em uma frase
Etiquetas classificam casos e suítes e podem ser usadas na linha de comando para incluir, excluir ou exigir combinações.

## Por que importa
Recortes por etiqueta permitem rodar subconjuntos relevantes em cada momento sem duplicar arquivos de teste.

## Como funciona
Defina um vocabulário pequeno de etiquetas por risco, área ou tipo de verificação e mantenha a consistência entre arquivos.

## Exemplo
Uma execução de fumaça pode selecionar apenas casos marcados como críticos, deixando a suíte completa para a esteira noturna.

## Limites e trade-offs
Etiquetas contraditórias excluem casos sem aviso, e o uso de termos livres leva a filtros que não encontram nada.

## Como verificar
Liste os casos com uma combinação de etiquetas e compare com a execução filtrada para confirmar que a seleção corresponde à intenção.

## Conexões
- [[robot-setup-teardown]] — Veja também: Robot Framework: preparar e limpar em níveis distintos.
- [[robot-teardown-and-continuation]] — Veja também: Robot Framework: continuar após falhas quando faz sentido.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
