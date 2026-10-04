---
id: software.devops.tranche12.001194
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://just.systems/man/en/", "https://raw.githubusercontent.com/casey/just/master/README.md", "https://github.com/casey/just"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# just: Receitas Shebang (#!/usr/bin/env) para Execução em Bloco Único e Múltiplas Linguagens

## Em uma frase
No `just`, receitas comuns executam cada linha em um sub-processo de shell separado, mas receitas que começam com uma linha shebang (`#!/usr/bin/env bash`, `#!/usr/bin/env python3`, `#!/usr/bin/env node`) são salvas em um arquivo temporário e executadas como um único script contínuo pelo interpretador escolhido.

## Por que importa
Em receitas linha-a-linha (tanto no `make` quanto no modo padrão do `just`), rodar `cd subpasta` ou definir uma variável local `FOO=bar` na primeira linha não tem efeito na segunda linha, pois cada linha roda num shell distinto.

## Como funciona
Ao iniciar o corpo da receita com `#!/usr/bin/env bash` seguido de `set -euo pipefail`, todas as linhas subsequentes compartilham o mesmo processo, diretório de trabalho (`cd`), variáveis locais e traps; além disso, é possível escrever receitas inteiras em Python, Ruby, Nu ou Node.js diretamente dentro do `justfile`.

## Exemplo
```just
verifica-manifestos cluster="staging":
  #!/usr/bin/env bash
  set -euo pipefail
  cd "clusters/{{cluster}}"
  for f in *.yaml; do
    echo "Validando $f em $(pwd)"
    kubectl apply --dry-run=client -f "$f"
  done
```

## Limites e trade-offs
Omitir `set -euo pipefail` dentro de uma receita shebang `#!/usr/bin/env bash` faz com que erros em linhas intermediárias do script sejam ignorados pelo Bash, pois o flag `-e` automático do `just` só se aplica a receitas linha-a-linha.

## Como verificar
Adicione sempre `set -euo pipefail` logo abaixo de `#!/usr/bin/env bash` em toda receita shebang no `justfile`.

## Conexões
- [[just-settings-set-shell-dotenv-load-positional-arguments-export]] — Veja também: just: Configurações de Comportamento no justfile (set shell, dotenv-load, export e positional-arguments).
- [[just-expressoes-funcoes-embutidas-arch-os-env-var-sha256]] — Veja também: just: Linguagem de Expressões, Condicionais e Funções Embutidas (os(), arch(), env_var(), sha256()).

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
