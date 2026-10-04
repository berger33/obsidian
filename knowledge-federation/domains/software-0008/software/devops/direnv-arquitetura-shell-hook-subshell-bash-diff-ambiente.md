---
id: software.devops.tranche12.001131
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
fontes: ["https://raw.githubusercontent.com/direnv/direnv/master/README.md", "https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md", "https://github.com/direnv/direnv"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# direnv: Arquitetura de Hook de Prompt e Captura de Diff de Ambiente via Sub-Shell Bash

## Em uma frase
O `direnv` é uma extensão compilada em um único binário estático e agnóstica de linguagem que carrega e descarrega variáveis de ambiente automaticamente conforme o usuário navega entre diretórios no terminal, mantendo o `~/.profile` e o `~/.zshrc` limpos.

## Por que importa
Acumular dezenas de `export AWS_PROFILE=...`, `export KUBECONFIG=...` e caminhos `PATH` de projetos distintos dentro do `~/.bashrc` ou `~/.zshrc` causa colisão de credenciais entre clientes e aplica configurações erradas quando o operador muda de pasta.

## Como funciona
Antes de exibir cada prompt do terminal, o hook do `direnv` verifica a existência de um arquivo `.envrc` (e opcionalmente `.env`) no diretório atual ou em diretórios pais. Se o arquivo existir e estiver criptograficamente autorizado, o `direnv` executa o `.envrc` dentro de um sub-processo **bash** isolado, captura apenas a diferença das variáveis exportadas (`environment diff`) e aplica ou reverte esse diff no shell atual (seja `bash`, `zsh`, `fish`, `nushell`, `elvish`, `tcsh` ou `pwsh`).

## Exemplo
```bash
mkdir -p /tmp/demo-direnv && cd /tmp/demo-direnv
echo 'export KUBECONFIG="$PWD/kubeconfig-homolog.yaml"' > .envrc
direnv allow .
echo "$KUBECONFIG"
cd /tmp
echo "${KUBECONFIG:-descarregado}"
```

## Limites e trade-offs
Definir aliases de shell (`alias k=kubectl`) ou funções bash dentro do `.envrc` esperando que eles fiquem disponíveis no shell interativo falha porque o `direnv` executa o `.envrc` num sub-processo e exporta apenas variáveis de ambiente de volta ao shell pai.

## Como verificar
Verifique as variáveis exportadas na linha `direnv export: +VAR` ao entrar no diretório e confirme que elas são removidas (`direnv: unloading`) ao sair com `cd ..`.

## Conexões
- [[direnv-seguranca-allow-deny-bloqueio-execucao-envrc]] — Veja também: direnv: Mecanismo de Segurança com direnv allow, direnv deny e Hash de Autorização.

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
