---
id: software.criacao_ia.tranche04.000360
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html", "https://docs.godotengine.org/en/stable/engine_details/engine_api/custom_modules_in_cpp.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: godot-cpp versus módulos C++ — uma decisão de distribuição

## Em uma frase
A escolha entre GDExtension e módulo é de distribuição, não de performance crua: o mesmo compiled godot-cpp serve editor e projeto exportado, enquanto módulos entram no build estático do motor e obrigam recompilar templates.

## Por que importa
O texto oficial compara as duas vias e lista os dois lados da balança — a portabilidade da lib única contra o acesso profundo ao motor. Times que escolhem por ideologia ('módulo é mais rápido', 'extension é mais fácil') pagam nos detalhes: quem precisa de um hook interno do render driver numa extensão descobre tarde que GDExtension não alcança o que módulo alcança.

## Como funciona
A favor de godot-cpp (a doc, literal): 'use the same compiled godot-cpp library in the editor and exported project' (com módulos, é preciso recompilar todos os templates de export usados); 'godot-cpp only requires you to compile your library, not the whole engine'. A favor de módulos: integração mais profunda ('C++ modules provide deeper integration into the engine'), e features sem carregar arquivos nativos no export. A regra de ouro da própria doc: se algo é acessível só por módulo, abra issue no godot-cpp para discutir expor a funcionalidade — a fronteira é negociada, não fixa.

## Exemplo
Um codec de compressão próprio como extensão: uma release cobre editor+export de todas as plataformas com N binários por [libraries]. Um novo compositing pass que mexe no render pipeline: módulo, engine recompilada, templates próprios por plataforma — com o custo de release que isso implica.

## Limites e trade-offs
A performance das chamadas não decide entre as duas (ambas são código nativo compilado perto do motor); o que decide é o escopo de API e o custo de distribuição. 'Ideal if you need high-performance code you'd like to distribute as an add-on in the Asset Store' é o enquadramento de produto da extensão. E o canal 'abra uma issue' não é promessa de prazo — projetos de prazo fixo devem auditar a lista de funções alcançáveis antes de escolher.

## Como verificar
Antes de apostar na extensão: liste as APIs do motor de que seu código precisa e procure-as na doc de extensão_api.json do seu alvo. Um spike mínimo de um nó que faz o call mais crítico fecha a dúvida em dias. Revise a decisão a cada upgrade de engine — a lista de 'não alcançável via extensão' encurta com o tempo.

## Conexões
- [[gdextension-icone-svg-e-dependencies]] — Godot 4: [icons] e [dependencies] completam o .gdextension — com contrato de 16×16 px.

## Fontes
- [Godot — About godot-cpp](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html) — a seção 'Differences between godot-cpp and C++ modules' com os prós declarados de cada lado Consulta: 2026-10-04.
- [Godot — Custom C++ modules](https://docs.godotengine.org/en/stable/engine_details/engine_api/custom_modules_in_cpp.html) — a via alternativa, com o custo de compilar o motor descrito pela própria doc Consulta: 2026-10-04.
