---
id: software.seguranca.tranche07.000673
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/sudo-project/sudo/main/README.md", "https://www.sudo.ws/docs/man/sudoers.man/", "https://www.sudo.ws/docs/man/sudo_logsrvd.man/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sudoers: Pinagem Criptográfica de Binários e Scripts com **SHA-224 / SHA-256 / SHA-384 / SHA-512 Digest** no `/etc/sudoers`

## Em uma frase
Quando uma regra no `sudoers` autoriza um usuário ou automação de CI/CD a executar um script de manutenção customizado como `root` (ex.: `/usr/local/sbin/deploy-app.sh`), surge um risco clássico: se por um erro de permissão de diretório ou grupo o script puder ser modificado por um usuário sem privilégio, ele injeta um shell `root` dentro do script.

## Por que importa
Para eliminar esse vetor, a gramática do `sudoers` suporta **Pinagem de Hash Criptográfico (`sha224`, `sha256`, `sha384`, `sha512`)** diretamente antes do caminho do comando!

## Como funciona
Antes de executar o comando, o `sudo` abre o arquivo executável, calcula seu hash SHA-256 (em hexadecimal ou Base64) e **aborta imediatamente a execução se um único byte do binário ou script tiver sido alterado** em relação ao digest cravado na política `sudoers`.

## Exemplo
```sudoers
# /etc/sudoers.d/30-pinned-deploy — Autorizar execucao apenas se o hash SHA-256 do script for exatamente o aprovado
Cmnd_Alias DEPLOY_SCRIPT = sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 /usr/local/sbin/deploy-app.sh ""

deployer ALL = (root) NOPASSWD: DEPLOY_SCRIPT
```

## Limites e trade-offs
Observe as aspas vazias **`""`** ao final do caminho na regra acima (`/usr/local/sbin/deploy-app.sh ""`): na sintaxe do `sudoers`, colocar `""` após o comando **proíbe que o usuário passe quaisquer argumentos de linha de comando** (permitindo executar o comando exclusivamente sem argumentos), enquanto omitir `""` permitiria passar argumentos arbitrários!

## Como verificar
Calcule o digest com `openssl dgst -sha256 -binary /usr/local/sbin/deploy-app.sh | openssl base64` (ou `sha256sum`) e verifique com `sudo -l -U deployer` a exibição do `sha256:...` anexado ao comando.

## Conexões
- [[sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra]] — Veja também: Sudoers: Gramática de Especificação de Comandos, Aliases (`User_Alias`, `Runas_Alias`, `Host_Alias`, `Cmnd_Alias`) e a Regra **"Last Match Wins"**.
- [[sudo-prevencao-gtfobins-noexec-sudoedit-restricao-argumentos-curingas]] — Veja também: Sudoers: Prevenção de Escalação de Privilégio (**GTFOBins**) — Uso da Tag **`NOEXEC:`**, **`sudoedit` (`sudo -e`)** e Perigos do Curinga `*`.
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Referência cruzada direta com sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
