---
id: software.criacao_ia.tranche04.000354
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
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: compatibility_minimum e maximum são portas de carga, não metadados

## Em uma frase
Dois campos da seção [configuration] decidem em quais versões do motor a extensão é aceita: minimum barra engines antigas de carregar recursos novos; maximum barra engines novas de carregar extensões desatualizadas.

## Por que importa
Cada lado da janela protege um failure-mode diferente. Sem minimum, um Godot 4.0 tenta carregar uma extensão que usa APIs de 4.2 e o crash acontece longe do arquivo .gdextension, no meio da execução. Sem maximum, o usuário atualiza o motor, a extensão carrega sobre uma API que mudou, e os bugs aparecem como comportamento fantasma de uma lib nativa.

## Como funciona
A tabela oficial: 'compatibility_minimum — Minimum compatible version. This prevents older versions of Godot from loading extensions that depend on features from newer versions' (só a partir do 4.1); 'compatibility_maximum — prevents newer versions of Godot from loading the extension' (só a partir do 4.3). Declare minimum sempre igual ao alvo da compilação; use maximum ao saber de uma quebra não corrigida no binding, e suba-o conforme testar cada nova versão. Em motores sem suporte ao campo, o campo é ignorado — o suporte em si segue a regra de compatibilidade de versão.

## Exemplo
O add-on compilado contra 4.3 declara minimum=4.3; um usuário em 4.2 recebe o aviso de incompatibilidade na importação em vez de um SIGSEGV. Ao surgir a primeira falha reportada em 4.7-rc, um maximum temporário 4.6 compra tempo até o fix sair.

## Limites e trade-offs
Os campos são uma cortina de fumaça de segurança, não verificação: não validam sua ABI, só barram a carga. maximum permanente sem re-teste é como remover suporte de produto — defina expectativa de release. E o valor é string de versão — coerência com o alvo real do binding é manutenção sua.

## Como verificar
Mude o minimum do seu add-on para uma versão acima da sua engine de teste e confirme a recusa de carga com aviso legível. Faça o inverso com maximum. Numa versão de engine sem suporte ao campo (4.0/4.2), confirme o comportamento de ignorar — para documentar no README do seu produto.

## Conexões
- [[gdextension-alvo-baixo-compative-frente]] — Godot 4: mire a extensão na versão mais baixa que te atende, não na mais nova.
- [[gdextension-reloadable-dev-debug]] — Godot 4: reloadable recarrega a extensão — e é ferramenta de desenvolvimento, não de produção.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — a tabela [configuration] com as definições exatas e as notas de versão 4.1+/4.3+ Consulta: 2026-10-04.
- [Godot — About godot-cpp](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/about_godot_cpp.html) — o contexto de compatibilidade entre versões que os campos operacionalizam Consulta: 2026-10-04.
