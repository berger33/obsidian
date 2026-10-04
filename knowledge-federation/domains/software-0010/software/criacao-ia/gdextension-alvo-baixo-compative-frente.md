---
id: software.criacao_ia.tranche04.000353
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html", "https://docs.godotengine.org/en/stable/tutorials/migrating/upgrading_to_godot_4.1.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: mire a extensão na versão mais baixa que te atende, não na mais nova

## Em uma frase
A política de compatibilidade declarada: extensões mirando uma versão anterior do Godot devem funcionar em minors posteriores — nunca o contrário — e a escolha da versão-alvo determina quantos builds você mantém.

## Por que importa
Sem essa regra, o instinto é compilar contra o motor mais recente e 'funciona para todo mundo' — e é exatamente ao contrário: seu add-on vira refém de um único 4.x. A doc formaliza a estratégia: 'target the lowest version of Godot that has the features you need... This can save you from needing to create multiple builds'.

## Como funciona
Decida o alvo pela feature, não pela data: o binding godot-cpp tem branches por versão (4.x) que correspondem à release do motor, e você compila a extensão contra a API do alvo. A exceção documentada é histórica: extensões criadas para Godot 4.0 não funcionam em 4.1+ (houve quebra deliberada, com página própria de migração). E o status geral segue sendo de API em evolução — a doc registra que quebras podem acontecer para corrigir bugs maiores, o que torna o compatibility_maximum (abaixo) o cinto de segurança.

## Exemplo
Um plugin de importação nativa mira 4.2 (a versão mínima com o recurso de que precisa), declara compatibility_minimum = 4.2, e um único conjunto de binários cobre 4.2, 4.3, 4.4... até que uma quebra justificada o force a subir de alvo.

## Limites e trade-offs
Devem funcionar ≠ garantidamente funciona: a nota de status experimental autoriza quebra de compatibilidade em minor upgrades. Recursos que você não usa hoje mas pode querer amanhã podem mudar a escolha do alvo — a decisão é um trade-off registrado, não uma receita. E o alvo baixo não elimina o teste na versão mais nova: o custo de descobrir a quebra é do autor da extensão.

## Como verificar
Instale o par de versões do motor (alvo e mais nova) e carregue a mesma extensão nos dois: o teste é binário e em minutos. Na doc, confira que o exemplo de versão usada para compilar o binding corresponde ao seu alvo. Rode o upgrade de engine do projeto cliente com o add-on carregando — é o cenário real que a política protege.

## Conexões
- [[gdextension-entry-symbol-obrigatorio]] — Godot 4: entry_symbol é o contrato mínimo do arquivo .gdextension.
- [[gdextension-compatibility-min-max]] — Godot 4: compatibility_minimum e maximum são portas de carga, não metadados.

## Fontes
- [Godot — About godot-cpp: Version compatibility](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html) — enuncia a política de compatibilidade (inclusive a exceção do 4.0) e a estratégia de alvo baixo Consulta: 2026-10-04.
- [Godot — Upgrading to Godot 4.1](https://docs.godotengine.org/en/stable/tutorials/migrating/upgrading_to_godot_4.1.html) — página de migração referenciada pela nota de quebra das extensões de 4.0 Consulta: 2026-10-04.
