---
id: software.criacao_ia.tranche04.000355
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
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: reloadable recarrega a extensão — e é ferramenta de desenvolvimento, não de produção

## Em uma frase
O campo booleano reloadable permite à extensão ser recarregada ao ser recompilada, sem reiniciar o editor — com o suporte declarado como 'deve ser usado principalmente para desenvolver ou depurar'.

## Por que importa
O ciclo nativo no editor é o ponto doloroso clássico: recompilar, fechar o motor, reabrir, recriar o estado da cena. O reload corta esse ciclo. A ressalva da própria doc existe porque estado de runtime — ponteiros vivos, sinais conectados, singletons da sua lib — atravessa o reload por conta sua.

## Como funciona
Declare 'reloadable = true' na seção [configuration]. Suporte atual: 'reloading is supported for the godot-cpp binding in Godot 4.2 or later. Other language bindings may or may not support it as well.' Projete a lib para o reload: alocação de estado em structures gerenciadas pelo motor onde possível, sem estado global que dependa de endereços de função, e sem caches de objetos Godot crus que o desligar da lib invalidaria. Em CI de release, considere a decisão explícita de não depender de reload para o produto.

## Exemplo
O dev do plugin ativa reloadable, troca um parâmetro de filtro, 'Rebuild' no IDE e o editor recarrega com o comportamento novo em segundos; no build final o campo continua true — inofensivo, mas o time documenta que suporte a hot-reload não é garantido para bindings alternativos.

## Limites e trade-offs
Fora do godot-cpp ≥4.2 o comportamento é 'may or may not' — testar o seu binding antes de montar workflow em cima. Reload não é atualização a quente de dados: cenas com instâncias da lib podem precisar re-inicialização manual. E no export/runtime do jogador a flag não compra nada — é para a bancada.

## Como verificar
O teste é o ciclo: mude o output de um método, recompilie, confirme no editor que o comportamento mudou sem reiniciar. Com reloadable = false, confirme que nada muda até o reinício — a baseline. Rode o projeto com um binding comunitário para documentar empiricamente o suporte.

## Conexões
- [[gdextension-compatibility-min-max]] — Godot 4: compatibility_minimum e maximum são portas de carga, não metadados.
- [[gdextension-libraries-feature-tags]] — Godot 4: a seção [libraries] é um filtro por feature flags, não uma lista de caminhos.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — a linha da tabela com o suporte (godot-cpp 4.2+) e a ressalva de escopo dev/debug Consulta: 2026-10-04.
- [Godot — The GDExtension system (índice)](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/index.html) — a seção que reúne as páginas do mecanismo de carga Consulta: 2026-10-04.
