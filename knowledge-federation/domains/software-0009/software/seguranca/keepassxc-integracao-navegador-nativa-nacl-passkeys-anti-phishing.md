---
id: software.seguranca.tranche13.001205
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md", "https://keepassxc.org/docs/KeePassXC_UserGuide"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração Segura com Navegadores (**`keepassxc-proxy`**) e Suporte a **Passkeys (WebAuthn / FIDO2)** no KeePassXC: Prevenção contra Phishing de Domínio

## Em uma frase
Muitos profissionais desconfiam de extensões de navegador que sincronizam senhas na nuvem ou abrem portas HTTP locais (`localhost`) que qualquer site malicioso poderia tentar consultar via requisições Cross-Origin. Como a extensão oficial **KeePassXC-Browser** se comunica com o aplicativo desktop do KeePassXC sem abrir nenhuma porta de rede?

## Por que importa
A comunicação utiliza a API **Native Messaging** do navegador (Chrome, Firefox, Edge, Brave, Tor Browser) conectada ao binário local **`keepassxc-proxy`** via *stdin/stdout* e pipes/sockets locais autenticados, com **criptografia assimétrica autenticada de ponta a ponta (Curve25519 /XSalsa20-Poly1305 via libsodium/NaCl)** entre a extensão e o cofre após aprovação explícita da chave de associação pelo usuário!

## Como funciona
Além de preencher credenciais apenas quando a URL real da aba coincide com o domínio registrado na entrada (**proteção intrínseca contra páginas de Phishing/Evilginx com domínios falsos!**), o KeePassXC suporta armazenamento e autenticação de **Passkeys (WebAuthn / FIDO2)** diretamente dentro do cofre `.kdbx` através da integração com o navegador!

## Exemplo
```bash
# Verificar no sistema operacional a presenca do binario nativo keepassxc-proxy responsavel pela ponte Native Messaging
which keepassxc-proxy
keepassxc-proxy --version || true
```

## Limites e trade-offs
Nas configurações de **Browser Integration** do KeePassXC, mantenha ativada a opção *"Ask for permission before accessing credentials"* para entradas críticas de produção — exigindo um clique de confirmação explícita na janela nativa do KeePassXC antes que a extensão receba a credencial.

## Como verificar
Como a correspondência de URL é feita sobre o `origin` validado pelo próprio navegador, um site de phishing em `login-corp.attacker.com` jamais receberá o preenchimento automático da entrada cadastrada para `https://login.corp.interno`!

## Conexões
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Veja também: Automação de Segredos no Terminal com **`keepassxc-cli`**: Injetando Credenciais e TOTPs em Variáveis de Ambiente sem Expor no `.bash_history`.
- [[keepassxc-autotype-sequencias-customizadas-protecao-window-title]] — Veja também: Segurança do **Auto-Type (`Ctrl+Shift+V`)** no KeePassXC: Sequências Customizadas (`{USERNAME}{TAB}{PASSWORD}{TOTP}`), Delay e Validação de Título de Janela.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
