---
id: software.devops.tranche12.001137
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

# direnv: Extensões Pessoais e Corporativas em ~/.config/direnv/direnvrc e lib/*.sh

## Em uma frase
O `direnv` permite estender ou sobrescrever sua biblioteca padrão criando scripts Bash em `~/.config/direnv/direnvrc` ou arquivos modulares em `~/.config/direnv/lib/*.sh`, que são carregados automaticamente antes de qualquer `.envrc`.

## Por que importa
Repetir blocos complexos de código Bash (como buscar segredos no Vault/1Password, configurar proxies corporativos ou assumir roles AWS SSO) em dezenas de arquivos `.envrc` espalhados por repositórios dificulta a manutenção e polui os projetos.

## Como funciona
Funções definidas em `~/.config/direnv/lib/aws_sso.sh` (por exemplo, `use_aws_profile()`) ficam imediatamente disponíveis como primitivas declarativas para qualquer `.envrc` da máquina. Assim, o `.envrc` do projeto permanece enxuto (`use aws_profile staging-eks`) enquanto a implementação detalhada fica centralizada na configuração do usuário.

## Exemplo
```bash
mkdir -p ~/.config/direnv/lib
cat << 'EOF' > ~/.config/direnv/lib/kube_ctx.sh
use_kube_ctx() {
  export KUBECONFIG="$PWD/.kube/${1}.yaml"
  watch_file "$KUBECONFIG"
}
EOF
```

## Limites e trade-offs
Colocar comandos que produzem saída inesperada ou alteram variáveis globais fora de funções dentro de `~/.config/direnv/direnvrc` afeta todos os diretórios gerenciados pelo `direnv` na máquina.

## Como verificar
Encapsule toda extensão em `~/.config/direnv/lib/*.sh` dentro de funções nomeadas (`use_<recurso>` ou `layout_<tipo>`) e teste o carregamento com `direnv exec . env`.

## Conexões
- [[direnv-use-nix-use-flake-integracao-devbox-mise]] — Veja também: direnv: Funções use nix, use flake e Integração com Devbox e mise.
- [[direnv-isolamento-multi-cluster-kubeconfig-aws-profile-terraform]] — Veja também: direnv: Isolamento de Contexto Multi-Cluster e Multi-Cloud (KUBECONFIG, AWS_PROFILE e TF_WORKSPACE).

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
