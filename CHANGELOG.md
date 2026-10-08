# Changelog

Todas as alterações notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.5] - 2026-10-08

### Added
- Adicionado `CHANGELOG.md` com histórico completo de modificações.

## [1.0.4] - 2026-10-08

### Changed
- Migrado o endpoint da API de OpenCode Zen (`https://opencode.ai/zen/v1`) para OpenCode Go (`https://opencode.ai/zen/go/v1`).
- `const.py` passou a ser a única fonte da URL base da API.
- Atualizados metadados do fork (`manifest.json`):
  - `codeowners`: `@airy10` → `@wesiofilhoIF`
  - `documentation` e `issue_tracker` apontam para `wesiofilhoIF/opencodeGO_ha`
- Reescrito o `README.md` com instruções completas de instalação, configuração e solução de problemas em português.
- Atualizadas traduções (`strings.json` e `en.json`) para referenciar "OpenCode Go API key".
- Atualizado template de bug report para o nome do fork.

### Removed
- Removido `extra_body: {"require_parameters": True}`, específico do endpoint Zen.
- Removidos headers não padrão do OpenRouter (`X-Title` e `HTTP-Referer`) das chamadas de chat.

### Added
- Adicionado header `x-opencode-session` nas requisições de chat, conforme recomendado pela documentação do OpenCode Go.
- Adicionado `.gitignore` para excluir `__pycache__`, arquivos `.pyc` e configurações de IDEs.

### Fixed
- Corrigida divergência de URL em `__init__.py`, que ainda usava o endpoint antigo `/zen/v1` hardcoded.
- Corrigido domínio do botão "My Home Assistant" no `README.md` (`opencode` → `open_code`).
- Corrigido nome do logger no template de bug report (`custom_components.opencode_ha` → `custom_components.open_code`).

## [1.0.3] e anteriores

- Versões originais do repositório `airy10/opencode_ha`.
- Veja o histórico original em: https://github.com/airy10/opencode_ha/releases

---

[1.0.5]: https://github.com/wesiofilhoIF/opencodeGO_ha/releases/tag/v1.0.5
[1.0.4]: https://github.com/wesiofilhoIF/opencodeGO_ha/releases/tag/v1.0.4
[1.0.3]: https://github.com/airy10/opencode_ha/releases/tag/v1.0.3
