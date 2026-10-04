---
id: software.seguranca.tranche05.000484
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Modos de Transição de Execução (`ix`, `px`/`Px`, `cx`/`Cx`, `ux`/`Ux`) e Limpeza de Ambiente (*Environment Scrubbing*)

## Em uma frase
Quando um processo confinado pelo AppArmor invoca `execve()` para iniciar outro binário, a regra de execução no perfil deve especificar exatamente como o domínio de confinamento transitará: **`ix`** (*Inherit*), **`px`/`Px`** (*Discrete Profile*), **`cx`/`Cx`** (*Child Profile*) ou **`ux`/`Ux`** (*Unconfined*).

## Por que importa
A diferença entre a letra minúscula (`px`, `cx`, `ux`) e a **maiúscula (`Px`, `Cx`, `Ux`)** é crítica para a segurança: as variantes **maiúsculas** acionam o *Environment Scrubbing* da `glibc`/linker dinâmico, limpando variáveis perigosas como `LD_PRELOAD`, `LD_LIBRARY_PATH`, `PYTHONPATH` e `PATH` na transição de domínio.

## Como funciona
Usar `px` minúsculo sem limpeza de ambiente permite que o processo pai comprometido defina `LD_PRELOAD=/tmp/evil.so` antes de invocar o binário filho, injetando código dentro do novo perfil. Já **`Ux`/`ux`** retira o processo filho de qualquer confinamento e quase nunca deve ser usado em perfis de segurança; prefira sempre **`ix`** (herda o mesmo perfil) ou **`Px` / `Cx`** (transita para perfil próprio ou subperfil limpando o ambiente).

## Exemplo
```nginx
profile backup-runner /usr/local/sbin/backup-runner {
  #include <abstractions/base>

  # Herdar o mesmo perfil ao executar utilitarios basicos de compressao
  /usr/bin/gzip ixr,

  # Transitar para um subperfil dedicado limpando LD_PRELOAD/LD_LIBRARY_PATH (Cx maiusculo)
  /usr/bin/curl Cx -> curl_uploader,

  profile curl_uploader {
    #include <abstractions/base>
    #include <abstractions/ssl_certs>
    network inet stream,
    /usr/bin/curl mr,
    /var/backups/encrypted/*.tar.gz.enc r,
  }
}
```

## Limites e trade-offs
Se você definir `/usr/bin/helper Px,` (maiúsculo), mas não existir nenhum perfil carregado no kernel para `/usr/bin/helper`, a chamada `execve()` **falhará com `Permission denied`** (*fail-closed*); use `Pix` apenas se desejar fallback explícito para herança.

## Como verificar
Teste a execução do processo pai e verifique em `ps auxZ` que o processo filho `/usr/bin/curl` assumiu o contexto `backup-runner//curl_uploader (enforce)`.

## Conexões
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Veja também: AppArmor: Sintaxe de Regras de Perfil — Permissões de Arquivos (`r`, `w`, `a`, `k`, `l`, `m`), `capability`, `network`, `mount`, `ptrace` e `signal`.
- [[apparmor-abstracoes-tunables-local-overrides-manutencao-perfis]] — Veja também: AppArmor: Modularização com `abstractions/`, Variáveis `tunables/` e Customizações Seguras em `local/`.
- [[apparmor-subperfis-change-hat-pam-apparmor-mod-apparmor]] — Referência cruzada direta com apparmor-subperfis-change-hat-pam-apparmor-mod-apparmor.
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
